var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var CopyWebpackPlugin = require('copy-webpack-plugin');
var ExtractTextPlugin = require("extract-text-webpack-plugin");


var debug = process.argv.indexOf('--release') === -1;
var checkConfig = process.argv.indexOf('--check') !== -1;

// Shared config values
var context = path.resolve('pyconcz_2016', 'static');
var outputPath = path.resolve('pyconcz_2016', 'static_build');
var entry = ['./index'];
var plugins = [
  new BundleTracker({
    filename: './pyconcz_2016/static_build/webpack-stats.json'
  }),
  new CopyWebpackPlugin([
    { from: 'img', to: 'img' }
  ])
];
var output = {
    path: outputPath,
    filename: "js/[name]-[hash].js",
    publicPath: 'http://lan.pycon.cz:8001/'
};
var scssLoader;

// Release specific config
if (!debug) {
  plugins.push(
    new ExtractTextPlugin("css/styles.css")
  );

  output.publicPath = '/2016/static/';

  scssLoader = {
    test: /\.scss$/,
    loader: ExtractTextPlugin.extract('style', ['css', 'sass'])
  }
} else {
  entry.unshift(
    'webpack-dev-server/client?http://lan.pycon.cz:8001',
    'webpack/hot/only-dev-server'
  );

  plugins.unshift(
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin()
  );

  scssLoader = {
    test: /\.scss$/,
      loaders: ['style', 'css', 'sass']
  }
}


var config = {
  context: context,
  entry: entry,
  plugins: plugins,
  output: output,

  module: {
    loaders: [scssLoader]
  },

  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js']
  }
};

if (checkConfig) console.log(config);

module.exports = config;
