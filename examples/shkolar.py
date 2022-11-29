import sqloxide

view = "SELECT key:val::int FROM t1"

res = sqloxide.parse_sql(sql=view)

print (res)


# [package]
# name = "sqloxide"
# version = "1.1.156"
# authors = ["Shkolar"]
# edition = "2018"

# [lib]
# name = "sqloxide"
# crate-type = ["cdylib"]

# [dependencies]
# pythonize = "0.17"
# sqlparser = { git = "https://github.com/illumex-ai/sqlparser-rs" , branch = "feature/bracket", features = ["json_example"]}

# [dependencies.pyo3]
# version = "0.17.1"
# features = ["extension-module"]
