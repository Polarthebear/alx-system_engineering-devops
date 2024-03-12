#!/usr/bin/env ruby
# Regular expression that matches the cases of 'hbttn'.
puts ARGV[0].scan(/hbt{2,5}n/).join
