#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	parts = name.split("-")
	return f"Bonjour, {parts[0].capitalize()}"

def get_random_sentence(animals, adjectives, fruits):
	animal = random.choice(animals)
	adjective = random.choice(adjectives)
	fruit = random.choice(fruits)
	return f"Aujourd'hui, j'ai vu un {animal} s'emparer d'un panier {adjective} plein de {fruit}."

def encrypt(text, shift):
	text = text.upper()
	encrypted_text = ""
	for c in text:
		if c.isalpha():
			new_char = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
			encrypted_text += new_char
		else:
			encrypted_text += c
	
	return encrypted_text

def decrypt(encrypted_text, shift):
	decoded_text = ""
	for c in encrypted_text:
		if c.isalpha():
			new_char = chr((ord(c) - ord('A') + 26 - shift) % 26 + ord('A'))
			decoded_text += new_char
		else:
			decoded_text += c
	
	return decoded_text


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
