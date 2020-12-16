drop table if exists audiofingerprints;
create table audiofingerprints (id integer primary key autoincrement, filename text not null, full_path text not null, fingerprint text not null);
