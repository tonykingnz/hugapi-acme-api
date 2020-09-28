create table if not exists store(
	store_id serial primary key,
	name text unique not null,
	address text not null
);

create type category_type as enum ('service', 'product');

create table if not exists store_item(
	store_item_id serial primary key,
	name text unique not null,
	unit text not null,
	image text,
	category category_type not null,
	lastPrice money not null
);
