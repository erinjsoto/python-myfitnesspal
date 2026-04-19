import myfitnesspal

client = myfitnesspal.Client()

day = client.get_date(2013, 3, 2)
print(day)