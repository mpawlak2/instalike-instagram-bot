![some likes](https://s32.postimg.org/53zwfkat1/Screenshot_2016_05_25_05_20_06_1.png)

# avaiable features
- automated likes
- automated follows
- automated unfollows (requires database connection)

# configuration guide
Edit `default.cfg` file
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
  <tr id='opt16'>
    <td>DATABASE::UseDatabase</td>
    <td>If set to <code>True</code> all operations will be persisted in postgresql database that you must have installed. Below are setting. Set to <code>False</code> if you dont have database installed.</td>
  </tr>
  <tr id='opt17'>
    <td>DATABASE::DatabaseName</td>
    <td>Name of database you want to use.</td>
  </tr>
  <tr id='opt18'>
    <td>DATABASE::UserName</td>
    <td>Database user.</td>
  </tr>
  <tr id='opt19'>
    <td>DATABASE::Password</td>
    <td>Database password.</td>
  </tr>
  <tr id='opt20'>
    <td>DATABASE::Address</td>
    <td>Database host, <code>localhost</code> is default.</td>
  </tr>
  <tr id='opt21'>
    <td>DATABASE::LogOperations</td>
    <td>not working</td>
  </tr>
  <tr id='opt22'>
    <td>INSTALIKE::MaxLikesPerHour</td>
    <td>Estimate what max likes per hour should be, based on this setting wait times are calculated. <code>200</code> is default.</td>
  </tr>
  <tr id='opt23'>
    <td>INSTALIKE::Tags</td>
    <td>Specify tags that bot will use to find and like photos or follow users. Make sure to put comma between tags e.g. <code>tag1, tag2, tag3, tag4</code></td>
  </tr>
  <tr id='opt24'>
    <td>INSTAFOLLOW::MaxFollowsPerHour</td>
    <td>Max users that will be followed per hour. Default value is <code>8</code></td>
  </tr>
  <tr id='opt25'>
    <td>INSTAFOLLOW::MaxUnfollowsPerHour</td>
    <td>Max users that will be unfollowed per hour. Default value is <code>2</code>. Unfollowing functionality in progress.</td>
  </tr>
  <tr id='opt26'>
    <td>BLACKLIST::PhotoTagsList</td>
    <td>Specify tags that you would like to avoid. e.g. <code>comma, separated, list, format</code></td>
  </tr>
  <tr id='opt27'>
    <td>BLACKLIST::UserDescription</td>
    <td>Avoid users whose description contains any of these words. e.g. <code>comma, separated, list, format</code></td>
  </tr>
  <tr id='opt28'>
    <td>LIKEFILTER::MinLikesOnPhoto</td>
    <td>Do not like photos with less likes than specified value, default value is <code>0</code></td>
  </tr>
  <tr id='opt29'>
    <td>LIKEFILTER::MaxLikesOnPhoto</td>
    <td>Do not like photos with more likes than specified value, default value is <code>0</code> which is no limit</td>
  </tr>
</table>

# starting bot
If you have provided your username and password combination in `default.cfg` file then start with `python main.py` otherwise use `python main.py -u username -p password`


# requirements
- python 3.5+
- postgresql
- `python -m pip install requests`
- `python -m pip install py-postgresql`

# external libs docs
[py-postgresql docs](http://python.projects.pgfoundry.org/docs/1.1/)
