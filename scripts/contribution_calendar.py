"""Fetch and publish the real GitHub calendar; never substitute demo activity."""
import argparse
from datetime import date, datetime, timezone
from html import escape
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

QUERY = '''query($login:String!){user(login:$login){login contributionsCollection{totalCommitContributions restrictedContributionsCount contributionCalendar{totalContributions weeks{contributionDays{date contributionCount contributionLevel color}}}}}}'''
LEVELS = ['NONE','FIRST_QUARTILE','SECOND_QUARTILE','THIRD_QUARTILE','FOURTH_QUARTILE']


def validate(payload, username):
    """Reject failed API responses, wrong users and malformed daily measurements."""
    if payload.get('errors'):
        raise ValueError('GitHub rejected the calendar query; previous output must be preserved')
    user = payload.get('data', {}).get('user')
    if not user or user.get('login', '').lower() != username.lower():
        raise ValueError('calendar belongs to a different or unknown GitHub user')
    collection = user['contributionsCollection']
    calendar = collection['contributionCalendar']
    days = [day for week in calendar['weeks'] for day in week['contributionDays']]
    if not 350 <= len(days) <= 380:
        raise ValueError('expected a full-year GitHub calendar')
    seen=set()
    for day in days:
        stamp=date.fromisoformat(day['date'])
        count=day['contributionCount']
        if stamp in seen or type(count) is not int or count < 0 or day['contributionLevel'] not in LEVELS:
            raise ValueError('invalid or duplicate daily contribution measurement')
        seen.add(stamp)
    if sum(d['contributionCount'] for d in days) != calendar['totalContributions']:
        raise ValueError('daily measurements disagree with the GitHub total')
    return user, collection, calendar


def render(user, collection, calendar, mode, timestamp):
    """Static baseline lets readers compare animations against their recorded activity."""
    dark=mode=='dark'
    bg,ink,muted = ('#0d1117','#e6edf3','#9caac0') if dark else ('#ffffff','#172033','#59677b')
    colors=['#161b22','#0e4429','#006d32','#26a641','#39d353'] if dark else ['#ebedf0','#9be9a8','#40c463','#30a14e','#216e39']
    title=f"{user['login']} / {calendar['totalContributions']:,} contributions / {collection['totalCommitContributions']:,} commits"
    parts=[f'<rect width="980" height="190" rx="15" fill="{bg}"/>',f'<text x="36" y="28" fill="{ink}" font-size="16" font-weight="650">{escape(title)}</text>']
    for x,week in enumerate(calendar['weeks']):
        for day in week['contributionDays']:
            weekday=(date.fromisoformat(day['date']).weekday()+1)%7
            label=f"{day['date']}: {day['contributionCount']} contributions"
            parts.append(f'<rect x="{36+x*17}" y="{44+weekday*17}" width="13" height="13" rx="3" fill="{colors[LEVELS.index(day["contributionLevel"])]}"><title>{label}</title></rect>')
    parts.append(f'<text x="36" y="179" fill="{muted}" font-size="11">GitHub contribution calendar / {escape(timestamp)} UTC</text>')
    return '<svg xmlns="http://www.w3.org/2000/svg" width="980" height="190" viewBox="0 0 980 190" role="img" aria-label="'+escape(title)+'"><style>text{font-family:Segoe UI,Arial,sans-serif}</style>'+''.join(parts)+'</svg>\n'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--user',default='robgallardof')
    parser.add_argument('--output',type=Path,default=Path('dist'))
    args=parser.parse_args()
    token=os.environ.get('GITHUB_TOKEN')
    if not token:
        raise SystemExit('GITHUB_TOKEN is required; no sample calendar will be published')
    request=Request('https://api.github.com/graphql',data=json.dumps({'query':QUERY,'variables':{'login':args.user}}).encode(),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json','User-Agent':'robgallardof-profile-calendar'})
    with urlopen(request,timeout=45) as response:
        payload=json.load(response)
    user,collection,calendar=validate(payload,args.user)
    timestamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')
    args.output.mkdir(parents=True,exist_ok=True)
    for theme in ('light','dark'):
        (args.output/f'contributions-{theme}.svg').write_text(render(user,collection,calendar,theme,timestamp),encoding='utf-8')
    snapshot={'user':user['login'],'source':'https://api.github.com/graphql','generated_at_utc':timestamp,
              'total_contributions':calendar['totalContributions'],'total_commits':collection['totalCommitContributions'],'weeks':calendar['weeks']}
    (args.output/'contributions.json').write_text(json.dumps(snapshot,indent=2)+'\n',encoding='utf-8')
    print(f"Verified GitHub calendar for {user['login']}: {calendar['totalContributions']} contributions, {collection['totalCommitContributions']} commits")


if __name__=='__main__':
    main()
