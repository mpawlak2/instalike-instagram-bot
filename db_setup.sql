create table users 
	(id int primary key,
	username varchar(200) unique,
	full_name varchar(1000),
	profile_pic_url varchar(500),
	is_unpublished boolean,
	blocked_by_viewer boolean,
	is_private boolean);

create table photos 
	(id int primary key,
	code varchar(100) unique,
	width int,
	height int,
	is_ad boolean,
	likes_count int,
	is_video boolean,
	display_src varchar(500),
	loc varchar(500));--,
	--owner_fk integer REFERENCES users(id));

create table opcodes (
		id integer primary key,
		op_name varchar(100)
	);

insert into opcodes (id, op_name) values (1, 'like'), (2, 'unlike'), (3, 'follow'), (4, 'unfollow'), (5, 'block user'), (6, 'comment');
	
create table likes(id serial primary key, photo_id bigint REFERENCES photos (id), success boolean, status_code varchar(10))

create or replace function merge_photo(
	_id bigint,
	_width integer,
	_height integer,
	_code varchar,
	_is_ad boolean,
	_likes_count integer,
	_viewer_has_liked boolean,
	_is_video boolean,
	_display_src varchar,
	_location varchar)
returns boolean as $$
begin
	if _id is null then
		return false;
	end if;

	if photo_exists(_id) then
		update photos
		set
			likes_count = _likes_count,
			display_src = _display_src
		where id = _id;
	else
		insert into photos (id, code, width, height, is_ad, likes_count, is_video, display_src, loc)
		values (_id, _code, _width, _height, _is_ad, _likes_count, _is_video, _display_src, _location);
	end if;
	
	return true;
end;
$$ language plpgsql;

create or replace function photo_exists(photo_id bigint)
returns boolean
as $$
begin
	return exists(select null from photos where id = photo_id);
end
$$ language plpgsql;


create or replace function merge_activity(id bigint)
returns boolean
as $$
-- store activities from your account
begin

end
$$ language plpgsql;


create or replace function like_photo(_photo_id bigint, _success boolean, _status_code varchar(10))
returns boolean
as $$
begin

insert into likes (photo_id, success, status_code) values (_photo_id, _success, _status_code);
return true;

end
$$ language plpgsql;
