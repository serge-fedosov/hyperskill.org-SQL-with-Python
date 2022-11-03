you_need = "Write how many cups of coffee you will need:"
info = """For {} cups of coffee you will need:
{} ml of water
{} ml of milk
{} g of coffee beans"""

need_water = 200
need_milk = 50
need_coffee_beans = 15

print(you_need)
n = int(input())
print(info.format(n, n * need_water, n * need_milk, n * need_coffee_beans))
