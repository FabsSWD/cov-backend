from flask import Flask, jsonify

class MetricsController:
    def __init__(self, app):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/metrics', methods=['GET'])
        def metrics():
            metrics_data = {
                "models": ["raw", "bilateral", "canny"],
                "metrics": {
                    "accuracy": {
                        "raw": 0.96,
                        "bilateral": 0.90,
                        "canny": 0.85
                    },
                    "precision": {
                        "raw": 0.95,
                        "bilateral": 0.88,
                        "canny": 0.82
                    },
                    "recall": {
                        "raw": 0.94,
                        "bilateral": 0.89,
                        "canny": 0.84
                    }
                }
            }
            return jsonify(metrics_data)
