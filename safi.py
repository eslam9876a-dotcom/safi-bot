# بوت صافي - النسخة 1
def safi_reply(text):
    text = text.lower()
    if "سلام" in text or "هلا" in text:
        return "هلا والله! انا صافي معاك 😊"
    if "عامل ايه" in text:
        return "زي الفل الحمد لله، انت عامل ايه يا غالي؟"
    if "بحبك" in text:
        return "وانا كمان بحبك اوي ❤️"
    return "سمعتك! قول كمان"

print("بوت صافي اشتغل")
while True:
    m = input("انت: ")
    print("صافي:", safi_reply(m))
