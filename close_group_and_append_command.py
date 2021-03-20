import sublime
import sublime_plugin


class CloseGroupAndAppendCommand(sublime_plugin.WindowCommand):
    """
    Close current group and append all tabs to the back of previous group.
    If current group is the first group, close the next group instead.
    """
    def run(self):
        if self.window.num_groups() > 1:
            active_sheet = self.window.active_sheet()
            cur_group = max(1, self.window.active_group())  # at least 1
            prev_group = cur_group - 1
            prev_idx = len(self.window.sheets_in_group(prev_group))

            # append each sheet to the back of prev_group
            for sheet in self.window.sheets_in_group(cur_group):
                self.window.set_sheet_index(sheet, prev_group, prev_idx)
                prev_idx += 1

            self.window.run_command('close_pane')
            self.window.focus_sheet(active_sheet)
            self.window.status_message('Merge group complete.')
