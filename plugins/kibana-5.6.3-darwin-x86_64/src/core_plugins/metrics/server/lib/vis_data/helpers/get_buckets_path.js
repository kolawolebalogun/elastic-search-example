'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _lodash = require('lodash');

var _lodash2 = _interopRequireDefault(_lodash);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

exports.default = (id, metrics) => {
  const metric = _lodash2.default.find(metrics, { id });
  let bucketsPath = String(id);

  switch (metric.type) {
    case 'derivative':
      bucketsPath += '[normalized_value]';
      break;
    case 'percentile':
      const percentileKey = /\./.test(`${metric.percent}`) ? `${metric.percent}` : `${metric.percent}.0`;
      bucketsPath += `[${percentileKey}]`;
      break;
    case 'percentile_rank':
      bucketsPath += `[${metric.value}]`;
      break;
    case 'std_deviation':
    case 'variance':
    case 'sum_of_squares':
      if (/^std_deviation/.test(metric.type) && ~['upper', 'lower'].indexOf(metric.mode)) {
        bucketsPath += `[std_${metric.mode}]`;
      } else {
        bucketsPath += `[${metric.type}]`;
      }
      break;
  }

  return bucketsPath;
};

module.exports = exports['default'];
