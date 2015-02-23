import sublime, sublime_plugin

class wpStyleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region( 0, self.view.size(  ) )
		s = self.view.substr(region) 
		s = s.replace('    ','	')
		s = s.replace('(', '( ').replace(')', ' )').replace('	 )', '	)')
		s = s.replace('{', '{ ').replace('}', ' }').replace('	 }', '	}')
		s = s.replace('[', '[ ').replace(']', ' ]').replace('	 ]', '	]')
		s = s.replace('\n ','\n')
		s = s.replace(',', ', ')
		s = s.replace('!', '! ')
		s = s.replace(':\'', ': \'')
		s = s.replace(':f', ': f')
		s = s.replace(':[', ': [')
		s = s.replace(':{', ': {')
		s = s.replace('	*', '	 *')
		s = s.replace('	*/', '	 */')
		s = s.replace('\n* ', '\n * ')
		s = s.replace('\n*/', '\n */')
		s = s.replace('if(', 'if (')
		s = s.replace('for(', 'for (')
		s = s.replace('while(', 'while (')
		s = s.replace('  ', ' ')
		s = s.replace(' \r\n', '\r\n')
		s = s.replace(' \n', '\n')
		s = s.replace('( )', '()')
		s = s.replace('{ }', '{}')
		s = s.replace(' ,', ',')
		if not s[ -1: ] == '\n':
			s = s + '\r\n'
		self.view.replace( edit, region, s )

                

