from flask import Flask, jsonify


class MetricsController:
    def __init__(self, app):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/metrics', methods=['GET'])
        def metrics():
            metrics_data = {
                "models": {
                    "raw": {
                        "normal": 0.74,
                        "covid": 1.00,
                        "pneumonia": 1.00
                    },
                    "canny": {
                        "normal": 0.80,
                        "covid": 0.70,
                        "pneumonia": 1.00
                    },
                    "bilateral": {
                        "normal": 1.00,
                        "covid": 1.00,
                        "pneumonia": 0.67
                    }
                }
            }
            return jsonify(metrics_data)
