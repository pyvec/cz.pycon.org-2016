var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

var context = path.resolve('pyconcz_2016', 'static');

module.exports = {
  context: context,
  entry: [
    'webpack-dev-server/client?http://localhost:8001',
    'webpack/hot/only-dev-server',
    './index'
  ],

  output: {
      path: context,
      filename: "[name]-[hash].js",
      publicPath: 'http://localhost:8001/static/_build/'
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new BundleTracker({
      filename: './pyconcz_2016/static/_build/webpack-stats.json'
    })
  ],

  module: {
    loaders: [
      { test: /\.scss$/, loaders: ['style', 'css', 'sass']}
    ]
  },

  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js']
  }
};
