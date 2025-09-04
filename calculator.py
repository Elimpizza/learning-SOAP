import zeep

wsdl_url = "http://www.dneonline.com/calculator.asmx?WSDL"

client = zeep.Client(wsdl=wsdl_url)

print("1. Add")
print("2. Subtract") 
print("3. Multiply")
print("4. Divide")

operation = input("Operation >")

operation_map = {
    "1": client.service.Add,
    "2": client.service.Subtract,
    "3": client.service.Multiply,
    "4": client.service.Divide,
}

symbol_map = {
    "1": "+",
    "2": "-",
    "3": "*",
    "4": "/"
}

func = operation_map.get(operation)

if func:
    a = input("First arg > ")
    b = input("Second arg > ")
    symbol = symbol_map.get(operation)
    result = func(intA=int(a), intB=int(b))
    print(f"{a} {symbol} {b} = {result}")
else:
    print("Invalid operation")
