# a script that install a package
package { 'flask':
ensure   => '2.1.1',
provider => 'pip3',
}
