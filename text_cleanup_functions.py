# function to find and replace all cammelCase, dash and undreline joined words
import re


def split_words_by_space(text):
    # split camelCase
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text) 
    # replace underscores and dashes with spaces
    text = re.sub(r'[_-]+', ' ', text)  
    return text


# replace non-word characters (includind numbers) with space - regex
def remove_non_word_chars(text):
    cleaned_text = re.sub(r'[^A-Za-z\s]', ' ', text)
    return cleaned_text


# replace any special character with a space
def replace_special_characters(input_string):
    characters_to_replace = ['\n', '/r/', 'r/', '\r']   
    for char in characters_to_replace:
        input_string = input_string.replace(char, ' ')
    return input_string


# remove all extra white spaces - use regex
def remove_extra_white_spaces(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    return cleaned_text

