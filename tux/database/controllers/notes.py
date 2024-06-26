from prisma.models import Notes
from tux.database.client import db


class NotesController:
    def __init__(self) -> None:
        """
        Initializes the controller and connects to the notes table in the database.
        """
        self.table = db.notes

    async def get_all_notes(self) -> list[Notes]:
        """
        Retrieves all notes from the database.

        Returns
        -------
        list[Notes]
            A list of all notes from the database.
        """
        return await self.table.find_many()

    async def get_note_by_id(self, note_id: int) -> Notes | None:
        """
        Retrieves a note from the database based on the specified note ID.

        Parameters
        ----------
        note_id : int
            The ID of the note to retrieve.

        Returns
        -------
        Notes or None
            The note if found, otherwise None.
        """
        return await self.table.find_first(where={"id": note_id})

    async def create_note(
        self,
        user_id: int,
        moderator_id: int,
        note_content: str,
    ) -> Notes:
        """
        Creates a new note in the database with the specified user ID, moderator ID, and content.

        Parameters
        ----------
        user_id : int
            The ID of the user for whom the note is created.
        moderator_id : int
            The ID of the moderator who created the note.
        note_content : str
            The content of the note.

        Returns
        -------
        Notes
            The newly created note.
        """
        return await self.table.create(
            data={
                "user_id": user_id,
                "moderator_id": moderator_id,
                "content": note_content,
            }
        )

    async def delete_note(self, note_id: int) -> None:
        """
        Deletes a note from the database based on the specified note ID.

        Parameters
        ----------
        note_id : int
            The ID of the note to delete.

        Returns
        -------
        None
        """
        await self.table.delete(where={"id": note_id})

    async def update_note(self, note_id: int, note_content: str) -> Notes | None:
        """
        Updates a note in the database with the specified note ID and new content.

        Parameters
        ----------
        note_id : int
            The ID of the note to update.
        note_content : str
            The new content for the note.

        Returns
        -------
        Notes or None
            The updated note if successful, otherwise None if the note was not found.
        """
        return await self.table.update(
            where={"id": note_id},
            data={"content": note_content},
        )

    async def get_notes_by_user_id(self, user_id: int) -> list[Notes]:
        """
        Retrieves all notes from the database based on the specified user ID.

        Parameters
        ----------
        user_id : int
            The ID of the user to retrieve notes for.

        Returns
        -------
        list[Notes]
            A list of all notes for the specified user.
        """

        return await self.table.find_many(where={"user_id": user_id})

    async def get_notes_by_moderator_id(self, moderator_id: int) -> list[Notes]:
        """
        Retrieves all notes from the database based on the specified moderator ID.

        Parameters
        ----------
        moderator_id : int
            The ID of the moderator to retrieve notes for.

        Returns
        -------
        list[Notes]
            A list of all notes created by the specified moderator.
        """
        return await self.table.find_many(where={"moderator_id": moderator_id})
