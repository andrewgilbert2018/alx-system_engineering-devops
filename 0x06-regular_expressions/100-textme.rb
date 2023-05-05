#!/usr/bin/env ruby
#a ruby script the a sender phone number,reciever phone and flag
puts ARGV[0].scan(/i(?<=from:|to:|flags:).+?(?=\])/).join(',')
