import datetime

now = datetime.datetime.now()

with open("output.txt", "w") as f:
    f.write("Kode dijalankan otomatis pada: " + str(now))
