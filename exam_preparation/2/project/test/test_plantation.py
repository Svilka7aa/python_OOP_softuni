from project.plantation import Plantation
import unittest


class TestPlantation(unittest.TestCase):
    valid_size = 1000
    invalid_size = -1

    def setUp(self) -> None:
        self.plantation = Plantation(self.valid_size)

    def test__init_when_size_is_1_expect_correct_values(self):
        plantation = Plantation(self.valid_size)

        self.assertEqual(self.valid_size, plantation.size)
        self.assertDictEqual({}, plantation.plants)
        self.assertListEqual([], plantation.workers)

    def test__size_prop_when_value_is_0_expect_correct(self):
        plantation = Plantation(self.valid_size)
        plantation.size = self.valid_size + 1

        self.assertEqual(plantation.size, self.valid_size + 1)

    def test__size_prop_when_value_is_negative_expect_to_raise(self):
        with self.assertRaises(ValueError) as context:
            self.plantation.size = self.invalid_size

        self.assertIsNotNone(context.exception)
        self.assertEqual("Size must be positive number!", str(context.exception))
        self.assertEqual(self.valid_size, self.plantation.size)

    def test__hire_worker_when_new_worker_expect_success(self):
        worker = "Worker"
        result = self.plantation.hire_worker(worker)
        self.assertEqual(f"{worker} successfully hired.", result)
        self.assertIn(worker, self.plantation.workers)

    def test__hire_worker_when_existing_worker_expect_to_raise(self):
        worker = "Worker"
        self.plantation.hire_worker(worker)
        with self.assertRaises(ValueError) as context:
            self.plantation.hire_worker(worker)
        self.assertIsNotNone(context.exception)
        self.assertEqual("Worker already hired!", str(context.exception))

    def test_len__no_plants(self):
        pass

    def test_len__with_plants(self):
        pass

    def test_str__when_no_workers_expect_correct(self):
        expected = f"Plantation size: {self.valid_size}"
        actual = str(self.plantation)

        self.assertEqual(expected, actual.strip())

    def test_str__when_workers_and_no_plants_Expect_correct(self):
        workers = ["Worker1", "Worker2"]
        [self.plantation.hire_worker(w) for w in workers]
        expected = f"""Plantation size: {self.valid_size}
Worker1, Worker2"""

        actual = str(self.plantation)

        self.assertEqual(expected, actual.strip())

    def test_str_plants_and_workers_expect_correct(self):
        workers = ["Worker1", "Worker2"]
        [self.plantation.hire_worker(w) for w in workers]
        plants = ["plant1", "plant2"]
        plant3 = "plant3"
        [self.plantation.planting(workers[0], p) for p in plants]
        self.plantation.planting(workers[1], plant3)
        expected = f"""Plantation size: {self.valid_size}
Worker1, Worker2
Worker1 planted: {', '.join(plants)}
Worker2 planted: {plant3}"""

        actual = str(self.plantation)

        self.assertEqual(expected, actual.strip())

    def test_repr_no_workers(self):
        workers = []
        result = f"""Size: {self.plantation.size}
Workers: {", ".join(workers)}"""

        expected = repr(self.plantation)

        self.assertEqual(expected, result)

    def test_repr_workers(self):
        workers = ["worker1", "worker2"]
        self.plantation.hire_worker("worker1")
        self.plantation.hire_worker("worker2")

        result = f"""Size: {self.plantation.size}
Workers: {", ".join(workers)}"""
        expected = repr(self.plantation)

        self.assertEqual(expected, result)

    def test_planting__when_worker_not_exists_expect_to_raise(self):
        worker = "Worker"
        with self.assertRaises(ValueError) as context:
            self.plantation.planting(worker, "")

        self.assertEqual(
            f"Worker with name {worker} is not hired!",
            str(context.exception), )

    def test_planting__when_full__expect_to_raise(self):
        worker = "Worker"
        self.plantation.size = 0
        self.plantation.hire_worker(worker)

        with self.assertRaises(ValueError) as context:
            self.plantation.planting(worker, "plant")

        self.assertEqual(
            "The plantation is full!",
            str(context.exception), )

    def test_planting__when_worker_has_plants__expect_success(self):
        worker = "Worker"
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, "plant1")
        self.plantation.planting(worker, "plant2")

        self.assertDictEqual(
            {worker: ["plant1", "plant2"]},
            self.plantation.plants
        )

    def test_planting__when_worker_has_no_plants__expect_success(self):
        worker = "Worker"
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, "plant1")

        self.assertDictEqual(
            {worker: ["plant1"]},
            self.plantation.plants
        )

