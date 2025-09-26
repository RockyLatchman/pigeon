

class StorageController < ApplicationController
   get '/' do
     erb :storage
   end

   post '/add-item' do
   end

   put '/edit-item/:id' do
   end

   delete '/remove-item/:id' do
   end
end
