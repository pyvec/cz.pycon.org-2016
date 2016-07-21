var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require("extract-text-webpack-plugin");


var debug = !process.argv.includes('release');
var checkConfig = process.argv.includes('--check');


var context = path.resolve('pyconcz_2016', 'static');
var entry = ['./index'];
var plugins = [
  new BundleTracker({
    filename: './pyconcz_2016/static/_build/webpack-stats.json'
  })
];
var output = {
    path: context,
    filename: "[name]-[hash].js",
    publicPath: 'http://lan.pycon.cz:8001/static/_build/'
};

if (!debug) {
  plugins.push(
    new ExtractTextPlugin("styles.css")
  );

} else {
  entry.unshift(
    'webpack-dev-server/client?http://localhost:8001',
    'webpack/hot/only-dev-server'
  );

  plugins.unshift(
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin()
  );

  output.publicPath = 'https://static.pycon.cz';
}


var config = {
  context: context,
  entry: entry,
  plugins: plugins,
  output: output,

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

if (checkConfig) console.log(config);

module.exports = config;
