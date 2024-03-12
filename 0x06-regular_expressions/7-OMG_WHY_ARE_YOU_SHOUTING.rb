#!/usr/bin/env ruby
# Regular expression that matches ONLY matching capital letters.
puts ARGV[0].scan(/[A-Z]/).join
