# -*- coding: utf-8 -*-


from odoo import fields, models


class ProjectTemplate(models.Model):
    """Model for Project Template"""
    _name = "project.template"
    _description = "Project Template"

    name = fields.Char(string="Project Template")
    task_name = fields.Char(string="Name of the Tasks")
    tag_ids = fields.Many2many("project.tags", string="Tags")
    manager_id = fields.Many2one("res.users", string="Project Manager")
    date_start = fields.Date(string='Start Date')
    date = fields.Date(string='Expiration Date', tracking=True,
                       help="Date on which this project ends")
    task_ids = fields.One2many("project.task", "project_template_id", string="Tasks")

    def action_create_project(self):
        """Function for the button, to create Project"""
        self.env['project.project'].create({
            'name': self.name,
            'label_tasks': self.task_name,
            'user_id': self.manager_id.id,
            'tag_ids': self.tag_ids.ids,
            'date_start': self.date_start,
            'date': self.date,
            'task_ids': self.task_ids,
        })
