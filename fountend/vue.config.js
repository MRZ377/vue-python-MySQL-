const { defineConfig } = require('@vue/cli-service')
const https = require('https')
const path = require('path')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    host:'0.0.0.0',
    port:8080,
    allowedHosts:'all',
    proxy:{
      '/api':{
        target:'http://127.0.0.1:5000',
        changeOrigin:true,
      }
    }
  }
})
