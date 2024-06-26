# EMBED_STANDARDS.md

Welcome to the guide on how to effectively use and contribute to the embed system in our Discord bot projects. This document aims to establish some basic standards and best practices for creating and utilizing Discord embeds through our `EmbedCreator` class. By adhering to these standards, we ensure consistency, maintainability, and improve the overall quality of our bot's interactions with users.

## EmbedCreator Class Overview

The `EmbedCreator` class is a utility designed to facilitate the creation and customization of Discord embeds. It offers methods for setting up embeds according to different states (e.g., Default, Info, Error, Warning, Success, Poll), customizing various aspects of the embed (e.g., title, description, fields, thumbnails), and ensuring consistent aesthetic and thematic elements across all embeds generated by the bot.

### Key Methods

- `create_embed`: The core method for creating a customized embed based on a provided state, title, and description. Additional context or interaction objects can be provided to tailor the embed further.
- `create_default_embed`, `create_info_embed`, `create_error_embed`, etc.: Convenience methods that wrap around `create_embed` for specific embed states, providing a simplified interface for common use cases.
- `add_field`, `set_thumbnail`: Methods for adding fields and setting the thumbnail image of an embed, allowing for further customization.

## Embed Standards

### Consistency in Appearance

- **Colors**: Use the predefined colors in `CONST.EMBED_STATE_COLORS` to maintain visual consistency across embed states. Each color corresponds to a specific state (e.g., info, error) and should be used accordingly.
- **Icons**: Similarly, `CONST.EMBED_STATE_ICONS` provides icons for different states. These should be used in the author icon field to visually represent the state of the embed.
- **Thumbnails**: When using thumbnails, ensure they are relevant to the content of the embed and appropriately sized.

### Content Guidelines

- **Titling**: Titles should be concise and directly related to the content of the embed. Use a consistent capitalization style (e.g., Title Case) across all embeds.
- **Description**: Keep the description informative and to the point. Aim for clarity and brevity, ensuring the message is easily understandable.
- **Fields**: Use fields to organize information logically. Inline fields can be used for side-by-side information, but avoid cluttering the embed.

### Footer and Timestamps

- **User Info**: Embed footers should include a "Requested by [user]" note, leveraging the `get_footer` method. This personalizes the embed and identifies the requestor.
- **Timestamps**: Use the timestamp to indicate when the embed was generated or relevant to. This provides context and can be critical for time-sensitive information.

### User and Context Considerations

- Always consider the context (command context or interaction) and the user when generating embeds. Tailor the content and presentation to the situation and audience.
- Ensure that all embeds respect Discord's rate limits and content policies.

## Contribution Guidelines

When contributing to the `EmbedCreator` class or creating new embeds:

- **Adherence to Standards**: Ensure your contributions are in line with the guidelines set forth in this document.
- **Testing**: Thoroughly test embeds in various scenarios to catch any issues or inconsistencies before deployment.
- **Documentation**: Update documentation and add comments as necessary to maintain clarity and understanding of the code.
- **Feedback and Improvements**: Be open to feedback and willing to make improvements. Our standards and practices may evolve over time.

## Conclusion

By following these standards and utilizing the `EmbedCreator` class, we can create a cohesive and user-friendly experience across all bot interactions. Remember, the goal is not just to provide information but to do so in a way that is accessible, engaging, and visually appealing. Your contributions and adherence to these guidelines are vital to achieving this goal.

# JSON Payload Example
![alt text](resources/image.png)
> generated with discohook

### Notes:
- This is a webhook json payload for a standard embed, you can send this to a discord webhook to create an embed message if you don't want to use the discord.py library.

```json
{
  "content": null,
  "embeds": [
    {
      "title": "Title Here",
      "description": "description here",
      "color": 3447003,
      "fields": [
        {
          "name": "field 1",
          "value": "this is"
        },
        {
          "name": "field 2 (inline)",
          "value": "a",
          "inline": true
        },
        {
          "name": "field 3 (inline)",
          "value": "test",
          "inline": true
        }
      ],
      "footer": {
        "text": "Requested by Tux",
        "icon_url": "https://cdn.discordapp.com/avatars/1172803065779339304/510e1c7b910fa6cad73edceeaa8b17f7.png"
      },
      "timestamp": "1984-03-14T04:20:00.000Z"
    }
  ],
  "attachments": []
}
```