package authenticate

default allow =false

allow {
input.user.role == "admin"
}

allow {
input.user.role == "data_admin"
input.user.type == "data"
input.path == "/data"
}

allow {
input.user.role == "data_admin"
input.user.type == "data"
startswith(input.path, "/data/")
input.method == "PUT"
}

allow {
input.user.role == "data_admin"
input.user.type == "data"
startswith(input.path, "/data/")
input.method == "DELETE"
}