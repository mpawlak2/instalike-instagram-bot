in progress..
<br/><br/>
![some likes](https://s32.postimg.org/53zwfkat1/Screenshot_2016_05_25_05_20_06_1.png)

# what works
- automated likes
- automated follows

# configuration guide
edit `default.cfg` file
<table>
  <tr>
    <th>Option</th>
    <th>Meaning</th>
  </tr>
  <tr id='opt0'>
    <td>BOT::WorkWholeTime</td>
    <td>If set to <code>True</code> bot will work whole time, no breaks. In other case periods will be in use.</td>
  </tr>
  <tr id='opt1'>
    <td>BOT::StopAfterNumerOfMinutes</td>
    <td>not working</td>
  </tr>
  <tr id='opt2'>
    <td>BOT::WorkHoursPerDay</td>
    <td>If option <code onmouseover='alert(1);'>BOT::WorkWholeTime</code> is set to <code>False</code> bot will work in 2 to 5 periods that sum up to that amount.</td>
  </tr>
  <tr id='opt3'>
    <td>BOT::IntelligentWorkingHours</td>
    <td>not working</td>
  </tr>
  <tr id='opt4'>
    <td>BOT::InstaLike</td>
    <td>If set to <code>True</code> bot will be liking photos.</td>
  </tr>
  <tr id='opt5'>
    <td>BOT::InstaFollow</td>
    <td>If set to <code>True</code> bot will be following users.</td>
  </tr>
  <tr id='opt6'>
    <td>BOT::InstaComment</td>
    <td>not working</td>
  </tr>
  <tr id='opt7'>
    <td>BOT::InstaMessage</td>
    <td>not working</td>
  </tr>
  <tr id='opt8'>
    <td>NOTIFICATIONS::EnableEmailSummaryNotifications</td>
    <td>not working</td>
  </tr>
  <tr id='opt9'>
    <td>NOTIFICATIONS::SendAttachment</td>
    <td>not working</td>
  </tr>
  <tr id='opt10'>
    <td>NOTIFICATIONS::EmailAdress</td>
    <td>not working</td>
  </tr>
  <tr id='opt11'>
    <td>NOTIFICATIONS::EmailServerAddress</td>
    <td>not working</td>
  </tr>
  <tr id='opt12'>
    <td>NOTIFICATIONS::EmailServerPassword</td>
    <td>not working</td>
  </tr>
  <tr id='opt13'>
    <td>BAN::DoNotGetBanned</td>
    <td>not working</td>
  </tr>
  <tr id='opt14'>
    <td>INSTAGRAM::Username</td>
    <td>Instagram username.</td>
  </tr>
  <tr id='opt15'>
    <td>INSTAGRAM::Password</td>
    <td>Instagram password.</td>
  </tr>
</table>


# instalike
instagram profile management



### like algorithm

1. get photos
2. validate
3. randomly select 2-7 photos from valid ones
4. wait 10-30s
5. like
6. before each like wait x-5 to x+5s, repeat steps 5-6 till selected photos are liked
7. step 1

# requirements
- python 3.5.1
- postgresql
- `python -m pip install requests`
- `python -m pip install py-postgresql`

# useful
[py-postgresql docs](http://python.projects.pgfoundry.org/docs/1.1/)
