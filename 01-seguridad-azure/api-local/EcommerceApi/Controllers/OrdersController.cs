using Microsoft.AspNetCore.Mvc;
using EcommerceApi.Models;

namespace EcommerceApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    // In-memory storage for orders
    private static readonly List<Order> Orders = new();

    // Reference to products (in a real app, this would be injected)
    private static readonly List<Product> Products = new()
    {
        new Product { Id = 1, Name = "Laptop", Price = 999.99m, Stock = 10 },
        new Product { Id = 2, Name = "Mouse", Price = 29.99m, Stock = 50 },
        new Product { Id = 3, Name = "Keyboard", Price = 79.99m, Stock = 30 },
        new Product { Id = 4, Name = "Monitor", Price = 299.99m, Stock = 15 },
        new Product { Id = 5, Name = "USB Cable", Price = 9.99m, Stock = 100 }
    };

    /// <summary>
    /// Get all orders
    /// </summary>
    [HttpGet]
    public ActionResult<IEnumerable<Order>> GetAllOrders()
    {
        return Ok(Orders);
    }

    /// <summary>
    /// Get an order by ID
    /// </summary>
    [HttpGet("{id}")]
    public ActionResult<Order> GetOrderById(int id)
    {
        var order = Orders.FirstOrDefault(o => o.Id == id);
        if (order == null)
        {
            return NotFound(new { message = $"Order with ID {id} not found" });
        }

        return Ok(order);
    }

    /// <summary>
    /// Create a new order
    /// </summary>
    [HttpPost]
    public ActionResult<Order> CreateOrder([FromBody] CreateOrderRequest request)
    {
        if (request.ProductIds == null || !request.ProductIds.Any())
        {
            return BadRequest(new { message = "Order must contain at least one product" });
        }

        // Validate that all products exist
        var invalidProductIds = request.ProductIds
            .Where(pid => !Products.Any(p => p.Id == pid))
            .ToList();

        if (invalidProductIds.Any())
        {
            return BadRequest(new { message = $"Products not found: {string.Join(", ", invalidProductIds)}" });
        }

        // Calculate total
        decimal total = 0;
        foreach (var productId in request.ProductIds)
        {
            var product = Products.FirstOrDefault(p => p.Id == productId);
            if (product != null)
            {
                total += product.Price;
            }
        }

        var order = new Order
        {
            Id = Orders.Any() ? Orders.Max(o => o.Id) + 1 : 1,
            CreatedAt = DateTime.UtcNow,
            ProductIds = request.ProductIds,
            Total = total
        };

        Orders.Add(order);

        return CreatedAtAction(nameof(GetOrderById), new { id = order.Id }, order);
    }
}

public class CreateOrderRequest
{
    public List<int> ProductIds { get; set; } = new List<int>();
}
