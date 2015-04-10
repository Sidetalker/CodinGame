import sys, math

message = input()

response = ""
bits = "" 

for char in message:
	bits += format(int.from_bytes(char.encode(), 'big'), '07b')

print("bits:", bits, file=sys.stderr)

index = 0

while index < len(bits):
	print("bits[index]:", bits[index], file=sys.stderr)
	print("index", index, file=sys.stderr)

	if bits[index] == "0":
		response += "00 "

		while index < len(bits):
			print("Enter 0 block", file=sys.stderr)
			
			if bits[index] == "0":
				print("Found 0", file=sys.stderr)
				response += "0"
				print("response:", response, file=sys.stderr)
				index += 1
			else:
				print("Exit 0 block", file=sys.stderr)
				response += " "
				break
	else:
		response += "0 "

		while index < len(bits):
			print("Enter 1 block", file=sys.stderr)

			if bits[index] == "1":
				print("Found 1", file=sys.stderr)
				response += "0"
				print("response:", response, file=sys.stderr)
				index += 1
			else:
				print("Exit 1 block", file=sys.stderr)
				response += " "
				break

print(response)