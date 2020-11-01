drop table exists store;
create table if not exists store(
	store_id serial primary key,
	name text unique not null,
	address text not null
);

drop type if exists category_type;
create type category_type as enum ('service', 'product');

drop type if exists store_item;
create table if not exists store_item(
	store_id int4 not null,
	store_item_id serial primary key,
	name text unique not null,
	unit text not null,
	image text,
	category category_type not null,
	last_price money not null
);

drop type if exists status_type;
create type status_type as enum ('pending', 'accepted', 'rejected');

drop table if exists orders;
create table if not exists orders(
	store_id int4 not null,
	store_order_id int4 not null,
	customer_id int4 not null,
	confirmation_date time not null,
	status_order status_type not null,
	item text[] not null,
	primary key (customer_id, store_order_id, confirmation_date)
);
