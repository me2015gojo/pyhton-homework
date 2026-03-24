temperature = float(input("Enter the current temperature in Celsius: "))

if temperature >= 25:
    print("It's warm. You can definitely wear something light and soft.")
elif temperature >= 18:
    print("It's a bit cold. A light t-shirt is perfect.")
elif temperature >= 10:
    print("It's a bit chilly. keep that pullover on .")
else:
    print("It's very cold. You definitely need your pullover or a heavy jacket.")