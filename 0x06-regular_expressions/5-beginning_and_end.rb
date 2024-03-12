#!/usr/bin/env ruby
# Regular expression that matches the cases that
# start with h and ends with n.
puts ARGV[0].scan(/h.n/).join
