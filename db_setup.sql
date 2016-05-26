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
	loc varchar(500),
	owner_fk integer REFERENCES users(id));
	

create or replace function merge_photo(
	id bigint,
	width integer,
	height integer,
	code varchar,
	is_ad boolean,
	likes_count integer,
	viewer_has_liked boolean,
	is_video boolean,
	display_src varchar,
	location varchar)
returns boolean as $$
begin
	if id is null then
		return false;
	end if;

	if photo_exists(id) then
		return false;
	end if;

	insert into photos (id, code, width, height, is_ad, likes_count, is_video, display_src, loc)
	values (id, code, width, height, is_ad, likes_count, is_video, display_src, location);
	
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