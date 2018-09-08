def greeter(name):
    return "hello " + name + "!"

print(greeter("Stan"))

#hello_name
def hello_name(name):
  return "Hello " + name + "!"

#make_abba
def make_abba(a, b):
  return a+b+b+a

#make_tags
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

#make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#extra_end
def extra_end(str):
  return str[-2:] + str[-2:] + str[-2:]


#first_two what

#first_half
def first_half(str):
  a = len(str)/2
  return str[:a]
  
#without_end
def without_end(str):
  return str[1:-1]

#combo_string
def combo_string(a, b):
  x = len(a)
  y = len(b)
  if x>=y:
    return b+a+b
  else:
    return a+b+a

#non_start
def non_start(a, b):
  return a[1:] + b[1:]

