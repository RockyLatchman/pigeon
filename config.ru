require 'sinatra/base'
require 'dotenv'
Dotenv.load
ENV['RACK_ENV'] ||= 'development'
Dir.glob('./{helpers,controllers}/*.rb').each { |file| require file}


map('/') { run ApplicationController }
map('/inbox') { run MessageController }
map('/account') { run AccountController }
map('/contacts') { run ContactController }
map('/settings') { run SettingsController }
map('/storage') { run StorageController }
