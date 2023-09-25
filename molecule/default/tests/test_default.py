"""Test install and run zeppelin service."""
import os
import time
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_zeppelin_unit(host):
    """Test zepplin service."""
    zpln = host.service('zeppelin')
    assert zpln.is_running
    assert zpln.is_enabled


def test_zeppelin_service(host):
    """Test adcm service."""
    for _ in range(30):
        try:
            output = host.check_output("curl http://localhost:8080/#/")
            break
        except AssertionError:
            time.sleep(1)
    assert host.socket('tcp://0.0.0.0:8080').is_listening
    assert 'Zeppelin' in output
