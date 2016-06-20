var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: [
    'webpack-dev-server/client?http://localhost:8001',
    'webpack/hot/only-dev-server',
    './static/index'
  ],

  output: {
      path: path.resolve('./static/'),
      filename: "[name]-[hash].js",
      publicPath: 'http://localhost:8001/static/_build/'
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new BundleTracker({filename: './static/_build/webpack-stats.json'})
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
