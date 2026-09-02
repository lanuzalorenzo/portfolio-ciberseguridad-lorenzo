using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;
using EcommerceApi.Models;

namespace EcommerceApi.Controllers;

[ApiController]
[Route("api/[controller]")]
[Authorize]
public class ProductsController : ControllerBase
{
    // In-memory storage for products
    private static readonly List<Product> Products = new()
    {
        new Product { Id = 1, Name = "Laptop", Price = 999.99m, Stock = 10 },
        new Product { Id = 2, Name = "Mouse", Price = 29.99m, Stock = 50 },
        new Product { Id = 3, Name = "Keyboard", Price = 79.99m, Stock = 30 },
        new Product { Id = 4, Name = "Monitor", Price = 299.99m, Stock = 15 },
        new Product { Id = 5, Name = "USB Cable", Price = 9.99m, Stock = 100 }
    };

    /// <summary>
    /// Get all products
    /// </summary>
    [HttpGet]
    public ActionResult<IEnumerable<Product>> GetAllProducts()
    {
        return Ok(Products);
    }

    /// <summary>
    /// Get a product by ID
    /// </summary>
    [HttpGet("{id}")]
    public ActionResult<Product> GetProductById(int id)
    {
        var product = Products.FirstOrDefault(p => p.Id == id);
        if (product == null)
        {
            return NotFound(new { message = $"Product with ID {id} not found" });
        }

        return Ok(product);
    }

    /// <summary>
    /// Create a new product
    /// </summary>
    [HttpPost]
    public ActionResult<Product> CreateProduct([FromBody] Product product)
    {
        if (string.IsNullOrWhiteSpace(product.Name))
        {
            return BadRequest(new { message = "Product name is required" });
        }

        if (product.Price < 0)
        {
            return BadRequest(new { message = "Price must be positive" });
        }

        if (product.Stock < 0)
        {
            return BadRequest(new { message = "Stock must be positive" });
        }

        product.Id = Products.Any() ? Products.Max(p => p.Id) + 1 : 1;
        Products.Add(product);

        return CreatedAtAction(nameof(GetProductById), new { id = product.Id }, product);
    }
}
