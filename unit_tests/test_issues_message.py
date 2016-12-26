from nose.tools import assert_equals

from StringIO import StringIO

class TestTrashPutIssueMessage:

    def setUp(self):
        self.out = StringIO()

    def test_trash_put_last_line(self):
        from trashcli.put import TrashPutCmd

        cmd = TrashPutCmd(self.out, StringIO(), None, None)
        cmd.run(['', '--help'])

        self.assert_last_line_of_output_is(
                'Report bugs to https://github.com/andreafrancia/trash-cli/issues')

    def test_trash_empty_last_line(self):
        from trashcli.trash import EmptyCmd

        cmd = EmptyCmd(self.out, StringIO(), [], lambda:[], now = None)
        cmd.run('', '--help')

        self.assert_last_line_of_output_is(
                'Report bugs to https://github.com/andreafrancia/trash-cli/issues')

    def test_trash_list_last_line(self):
        from trashcli.trash import ListCmd

        cmd = ListCmd(self.out, None, None, None, None)
        cmd.run('', '--help')

        self.assert_last_line_of_output_is(
                'Report bugs to https://github.com/andreafrancia/trash-cli/issues')

    def assert_last_line_of_output_is(self, expected):
        output = self.out.getvalue()
        if len(output.splitlines()) > 0:
            last_line = output.splitlines()[-1]
        else:
            last_line = ''
        assert_equals(expected, last_line,
                ('Last line of output should be:\n\n%s\n\n' % expected +
                'but the output is\n\n%s' % output))
