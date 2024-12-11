import unittest
import os
import subprocess


class TestDataPipeline(unittest.TestCase):
    def setUp(self):
        # Ensure the output directory exists
        self.output_dir = os.path.abspath('./data')
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def test_data_pipeline(self):
        # Run the data pipeline script
        script_path = os.path.abspath('./project/pipeline.sh')
        result = subprocess.run(['bash', script_path], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, msg=f"Pipeline script failed with error: {result.stderr}")

        # Check if the output files exist
        flood_file = os.path.join(self.output_dir, 'flood.csv')
        hpi_file = os.path.join(self.output_dir, 'hpi.csv')
        self.assertTrue(os.path.isfile(flood_file), msg="flood.csv does not exist")
        self.assertTrue(os.path.isfile(hpi_file), msg="hpi.csv does not exist")


if __name__ == '__main__':
    unittest.main()
