#!/usr/bin/env ruby
puts ARGV[0].scan((/i(?<=from:|to:|flags:).+?(?=\])/)).join(',')
