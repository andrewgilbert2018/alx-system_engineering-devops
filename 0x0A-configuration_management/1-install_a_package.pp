# a script that install a package
package { 'puppet-lint':
ensure   => '2.1.1',
provider => 'gem',
}
