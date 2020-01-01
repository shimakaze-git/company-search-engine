var users = [
  {
    user: "user",
    pwd: "password",
    roles: [
      {
        role: "dbOwner",
        db: "company_search_engine"
      }
    ]
  }
];

for (var i = 0, length = users.length; i < length; ++i) {
  db.createUser(users[i]);
}
