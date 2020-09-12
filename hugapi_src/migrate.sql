create table if not exists store(
	store_id serial primary key,
	name text unique not null,
	address text not null
);
