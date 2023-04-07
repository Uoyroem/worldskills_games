const path = require('node:path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    mode: 'development',
    entry: {
        index: path.join(__dirname, 'ts/index.ts'),
        add_appearance: path.join(__dirname, 'ts/add_appearance.ts'),
        game_detail: path.join(__dirname, 'ts/game_detail.ts')
    },
    output: {
        path: path.join(__dirname, 'build'),
        filename: '[name].js'
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'index.css'
        })
    ],
    module: {
        rules: [
            {
                test: /\.[tj]s$/,
                loader: 'babel-loader'
            },
            {
                test: /\.(sc|sa|c)ss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader',
                        options: {
                            sourceMap: true
                        }
                    },
                    'sass-loader'
                ]
            },
            {
                test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)$/,
                type: 'asset'
            },
        ]
    },
    devServer: {
        hot: true,
        compress: true,
        devMiddleware: {
            writeToDisk: true
        }
    }
};

