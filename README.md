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
  <tr>
    <td>BOT::WorkWholeTime</td>
    <td>If set to <code>True</code> bot will work whole time, no breaks. In other case periods will be in use.</td>
  </tr>
  <tr>
    <td>BOT::BotWorkAtDay</td>
    <td>If set to <code>True</code> bot will work from between specified hours. Requires option <code>BOT::WorkWholeTime</code> set to <code>True</code>.</td>
  </tr>
  <tr>
    <td>BOT::StopAfterNumerOfMinutes</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>BOT::WorkHoursPerDay</td>
    <td>If option <code onmouseover='alert(1);'>BOT::WorkWholeTime</code> is set to <code>False</code> bot will work in 2 to 5 periods that sum up to that amount.</td>
  </tr>
  <tr>
    <td>BOT::StartHour</td>
    <td>Requires option <code>BOT::WorkAtDay</code> set to <code>True</code>. Specify hour at which bot should start working.</td>
  </tr>
  <tr>
    <td>BOT::EndHour</td>
    <td>Requires option <code>BOT::WorkAtDay</code> set to <code>True</code>. Specify hour at which bot should stop working.</td>
  </tr>
  <tr>
    <td>BOT::LogDBOperations</td>
    <td>Whether or not to log db queries. <code>True</code> or <code>False</code>.</td>
  </tr>
  <tr>
    <td>BOT::InstaLike</td>
    <td>If set to <code>True</code> bot will be liking photos.</td>
  </tr>
  <tr>
    <td>BOT::InstaFollow</td>
    <td>If set to <code>True</code> bot will be following users.</td>
  </tr>
  <tr>
    <td>BOT::InstaComment</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>BOT::InstaMessage</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>NOTIFICATIONS::EnableEmailSummaryNotifications</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>NOTIFICATIONS::SendAttachment</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>NOTIFICATIONS::EmailAdress</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>NOTIFICATIONS::EmailServerAddress</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>NOTIFICATIONS::EmailServerPassword</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>BAN::DoNotGetBanned</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>INSTAGRAM::Username</td>
    <td>Instagram username.</td>
  </tr>
  <tr>
    <td>INSTAGRAM::Password</td>
    <td>Instagram password.</td>
  </tr>
  <tr>
    <td>DATABASE::UseDatabase</td>
    <td>If set to <code>True</code> all operations will be persisted in postgresql database that you must have installed. Below are setting. Set to <code>False</code> if you dont have database installed.</td>
  </tr>
  <tr>
    <td>DATABASE::DatabaseName</td>
    <td>Name of database you want to use.</td>
  </tr>
  <tr>
    <td>DATABASE::UserName</td>
    <td>Database user.</td>
  </tr>
  <tr>
    <td>DATABASE::Password</td>
    <td>Database password.</td>
  </tr>
  <tr>
    <td>DATABASE::Address</td>
    <td>Database host, <code>localhost</code> is default.</td>
  </tr>
  <tr>
    <td>DATABASE::LogOperations</td>
    <td>not working</td>
  </tr>
  <tr>
    <td>INSTALIKE::MaxLikesPerHour</td>
    <td>Estimate what max likes per hour should be, based on this setting wait times are calculated. <code>200</code> is default.</td>
  </tr>
  <tr>
    <td>INSTALIKE::Tags</td>
    <td>Specify tags that bot will use to find and like photos or follow users. Make sure to put comma between tags e.g. <code>tag1, tag2, tag3, tag4</code></td>
  </tr>
  <tr>
    <td>INSTAFOLLOW::MaxFollowsPerHour</td>
    <td>Max users that will be followed per hour. Default value is <code>8</code></td>
  </tr>
  <tr>
    <td>INSTAFOLLOW::MaxUnfollowsPerHour</td>
    <td>Max users that will be unfollowed per hour. Default value is <code>2</code>. Unfollowing functionality in progress.</td>
  </tr>
  <tr>
    <td>INSTAFOLLOW::UnfollowAfterNoOfDays</td>
    <td>Unfollow users who do not follow you back after that amount of days. <code>6</code> is default</td>
  </tr>
  <tr>
    <td>BLACKLIST::PhotoTagsList</td>
    <td>Specify tags that you would like to avoid. e.g. <code>comma, separated, list, format</code></td>
  </tr>
  <tr>
    <td>BLACKLIST::UserNameBlacklist</td>
    <td>Don't like media posted by user with these names. Don't follow users with these names. Comma separated list e.g. <code>mickey15, hulk12, lover2020</code></td>
  </tr>
  <tr>
    <td>BLACKLIST::UserDescription</td>
    <td>Avoid users whose description contains any of these words. e.g. <code>comma, separated, list, format</code></td>
  </tr>
  <tr>
    <td>LIKEFILTER::MinLikesOnPhoto</td>
    <td>Do not like photos with less likes than specified value, default value is <code>0</code> which is no limit</td>
  </tr>
  <tr>
    <td>LIKEFILTER::MaxLikesOnPhoto</td>
    <td>Do not like photos with more likes than specified value, default value is <code>0</code> which is no limit</td>
  </tr>
</table>

# starting bot
If you have provided your username and password combination in `default.cfg` file then start with `python main.py` otherwise use `python main.py -u username -p password`


# requirements
- python 3+
- postgresql 9.5
- `python -m pip install requests`
- `python -m pip install py-postgresql`

# external libs docs
[py-postgresql docs](http://python.projects.pgfoundry.org/docs/1.1/)


<hr/>

interested in more advanced bot? contact me at mpawlak62@gmail.com
