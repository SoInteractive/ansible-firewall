from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_linux(SystemInfo):
    assert SystemInfo.type == 'linux'


def test_yum_packages(Package, SystemInfo):
    if SystemInfo.distribution == 'centos':
        present = [
            "iptables-services"
        ]
        if present:
            for package in present:
                p = Package(package)
                assert p.is_installed


def test_apt_packages(Package, SystemInfo):
    if SystemInfo.distribution == 'ubuntu':
        present = [
            "iptables-persistent"
        ]
        if present:
            for package in present:
                p = Package(package)
                assert p.is_installed


def test_services(Service, SystemInfo):
    present = [
        "iptables"
    ]
    if present and SystemInfo.distribution == 'centos':
        for service in present:
            s = Service(service)
            assert s.is_enabled
            assert s.is_running
